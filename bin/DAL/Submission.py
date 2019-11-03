#!/user/bin/python3


class Submission:
	@staticmethod
	def submission_detail_upsert(pg, submission):
		cur = pg.cursor()
		cur.execute(
			"select submission_detail_upsert(%s, %s, %s, %s, %s, %s)",
			(
				submission.id,
				submission.subreddit,
				999,  # submission.author,
				submission.title,
				submission.selftext,
				submission.created_utc
			)
		)
		cur.close()
		return True

	@staticmethod
	def submission_snapshot_insert(pg, submission):
		cur = pg.cursor()
		cur.execute(
			"select submission_snapshot_insert(%s, %s, %s, %s, %s, %s)",
			(
				submission.id,
				0,  # submission.rank,
				0,  # submission.upvotes,
				0,  # submission.downvotes,
				submission.num_comments,
				False,  # submission.is_hot
			)
		)
		cur.close()
		return True

	@staticmethod
	def submission_schedule_set(pg, submission_id):
		cur = pg.cursor()
		cur.execute(
			"select post_control_upsert(%s, %s)",
			(
				submission_id,

			)
		)
		cur.close()
		return True
