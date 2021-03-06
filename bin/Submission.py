from datetime import datetime

"""
Post Object: contains post information
"""

# Script relies on UTF-8 not ASCII or other char sets / inputs should be sanitized


class Submission (object):

	def __init__(self, lib, submission):
		"""
		Create our own post Object from the given prow submission object

		:param lib: Anu's LIB file
		:param submission: Submission object
		"""

		self.lib = lib

		if submission is None:

			self.title = None
			self.id = None
			self.url = None
			self.subreddit = None
			self.score = None
			self.upvote_ratio = None
			self.author = None
			self.created_utc = None

		else:

			self.title = submission.title
			self.id = submission.id
			self.url = submission.url
			self.subreddit = str(submission.subreddit)
			self.num_comments = submission.num_comments
			self.score = submission.score
			self.upvote_ratio = submission.upvote_ratio

			try:
				self.author = str(submission.author)
			except:
				# In case author is deleted or otherwise doesn't exist
				self.author = None
				lib.write_log(f'Submission {submission.id} does not have author.')

			# created date
			self.created_utc = datetime.utcfromtimestamp(submission.created_utc).strftime('%Y-%m-%d %H:%M:%S')

	def populate_from_praw(self, submission):
		self.title = submission.title
		self.id = submission.id
		self.url = submission.url
		self.subreddit = str(submission.subreddit)
		self.num_comments = submission.num_comments
		self.score = submission.score
		self.upvote_ratio = submission.upvote_ratio

		try:
			self.author = str(submission.author)
		except:
			# In case author is deleted or otherwise doesn't exist
			self.author = None
			self.lib.write_log(f'Submission {submission.id} does not have author.')

		# created date
		self.created_utc = datetime.utcfromtimestamp(submission.created_utc).strftime('%Y-%m-%d %H:%M:%S')