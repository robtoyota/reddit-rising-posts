"""
Description: Used to collect data from Reddit
"""

import bin.SubmissionFunctions as SubmissionFunctions
import bin.CommentFunctions as CommentFunctions
from .LIB import LIB


class DataCollector:

    # Start the data collector for subreddit. It is to collect submission and then collect comments for them
    # Input:String config,  String subreddit name
    # Output: None
    def __init__(self, subreddit=None, praw_q = None):
        output_name = "{}_output.log".format(subreddit)
        error_name = "{}_error.log".format(subreddit)
        lib = LIB(cfg="config/DataCollection.cfg", out_log=output_name, err_log=error_name)
        lib.write_log("Data Collector {}".format(subreddit))

        # while True: #TODO: untill given the terminate signal from parent
            # TODO: get submissions from reddit for the subreddit (Submissions.get_hot(subreddit='funny', limit = 10) for example)
            # for each submission
                # TODO: Upsert submission into database details
                # TODO: Get comments (Comments.get_root_comments(Post post))
                #for each comment in comments:
                    # TODO: Upsert comment into database details

            # TODO: Get all submissions from database that are due for data collection; collect and add snapshot

            # TODO: Get all comments from database that are due for data collection; collect and  add snapshot

            # TODO: Run decision making processes (these need to be though about some more, but they will update the polling interval based on some formulas)

        submissions = SubmissionFunctions.get_hot(lib=lib, subreddit=subreddit, limit=10, praw_q=praw_q)
        lib.write_log("Got {} submissions from {}".format(len(submissions),subreddit))
        lib.end()
        pass
