from bin.Submission import Submission
from bin.DAL.Submission import Submission as DAL_submission

"""
Submission functions: retrieves submission from subreddit
"""


def get_hot(lib=None, praw=None, subreddit=None, limit=None):
	"""
	Gets hot posts using PRAW

	:param lib: Anu's lib file
	:param praw: PRAW object
	:param subreddit: Specified Subreddit
	:param limit: Number of posts
	:return: List of submissions
	:rtype: list
	"""

	# Ensure lib, praw_instance and subreddit are not none
	if (lib is None) or (praw is None) or (subreddit is None):
		return None

	# Get hot submissions from subreddit limited by given value
	try:
		submissions = praw.subreddit(subreddit).hot(limit=limit)
	except Exception as e:
		lib.write_log("Failed to get hot submissions due to the exception: {}".format(str(e)))
		return None
	submission_list = []

	# Make submissions objects
	for submission in submissions:
		s = Submission(lib, submission)
		submission_list.append(s)
		lib.write_log(s.title)
	lib.write_log("Completed subreddit {}".format(subreddit))

	# Return submissions list
	return submission_list


def get_rising(lib=None, praw=None, subreddit=None, limit=None):
	"""
	Get rising posts using PRAW

	:param lib: Anu's lib file
	:param praw: PRAW object
	:param subreddit: Specified Subreddit
	:param limit: Number of posts
	:return: List of submissions
	:rtype: list
	"""

	# Ensure lib, praw_instance and subreddit are not none
	if (lib is None) or (praw is None) or (subreddit is None):
		return None

	# Get rising submissions from subreddit limited by given value
	try:
		submissions = praw.subreddit(subreddit).rising(limit=limit)
	except Exception as e:
		lib.write_log("Failed to get rising submissions due to the exception: {}".format(str(e)))
		return None
	submission_list = []

	# Make submissions objects
	for submission in submissions:
		s = Submission(lib, submission)
		submission_list.append(s)
		lib.write_log(s.title)
	lib.write_log("Completed subreddit {}".format(subreddit))
	# Return submissions list
	return submission_list


def get_top(lib=None, praw=None, subreddit=None, time_filter='all', limit=None):
	"""
	Get top posts using PRAW

	:param lib: Anu's lib file
	:param praw: PRAW object
	:param subreddit: Specified Subreddit
	:param time_filter: Specified time-filter
	:param limit: Number of posts
	:return: List of submissions
	:rtype: list
	"""

	# Ensure lib, praw_instance and subreddit are not none
	if (lib is None) or (praw is None) or (subreddit is None):
		print("missing something")
		return None

	# Get top submissions from subreddit limited by given value
	try:
		# time_filter – Can be one of: all, day, hour, month, week, year (default: all).
		submissions = praw.subreddit(subreddit).top(time_filter=time_filter, limit=limit)
	except Exception as e:
		lib.write_log("Failed to get top submissions due to the exception: {}".format(str(e)))
		return None
	submission_list = []

	# Make submissions objects
	for submission in submissions:
		s = Submission(lib, submission)
		submission_list.append(s)
		lib.write_log(s.title)
	lib.write_log("Completed subreddit {}".format(subreddit))

	# Return submissions list
	return submission_list


def submission_snapshot_praw_pull(lib=None, praw=None, submission=None):
	"""
	Retreives a submission snapshot by using the submission id

	:param lib:
	:param praw:
	:param submission:
	:return:
	"""

	# Ensure lib, praw_instance and submission_id are not none
	if (lib is None) or (praw is None) or (submission is None):
		return None

	# Get snapshot of submission
	snapshot = praw.submission(id=submission.id)

	# Make submission object
	s = Submission(lib, snapshot)

	# Return submission object
	return s


def submission_snapshot_db_push(lib=None, pg=None, submission=None):
	"""
	Submits updated submission object to database.

	:param lib:
	:param pg:
	:param submission:
	:return snapshot_inserted:
	"""

	# Ensure lib, praw_instance and submission_id are not none
	if (lib is None) or (pg is None) or (submission is None):
		return None

	try:
		snapshot_inserted = DAL_submission.submission_snapshot_insert(pg, submission)
	except Exception:
		lib.write_log("Failed to insert submission snapshot into db due to exception: {}".format(Exception))
		raise
	else:
		lib.write_log("Successfully inserted submission snapshot into db.")
	return snapshot_inserted
