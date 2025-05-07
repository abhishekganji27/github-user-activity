import collections

class Activity:
    def __init__(self):
        self.push_db = collections.defaultdict(int)
        self.commit_cmt_db = collections.defaultdict(int)
        self.create_db = collections.defaultdict(int)
        self.delete_db = collections.defaultdict(int)
        self.fork_db = 0
        self.not_supported = set()


    def push_event_handler(self, event_obj):
        commit_cnt = event_obj['payload']['size']
        repo_name = event_obj['repo']['name']
        self.push_db[repo_name] += commit_cnt

    def commit_comment_handler(self, event_obj):
        repo_name = event_obj['repo']['name']
        self.commit_cmt_db[repo_name] += 1
    
    def create_handler(self, event_obj):
        ref_type = event_obj['payload']['ref_type']
        self.create_db[ref_type] += 1

    def delete_handler(self, event_obj):
        ref_type = event_obj['payload']['ref_type']
        self.delete_db[ref_type] += 1
    
    def fork_handler(self, event_obj):
        self.fork_db += 1

    def helper(self, handler, event_obj):
        # passes the event obj to the handler function.
        handler(event_obj)
        
    def final_summary(self):
        push = f"- Pushed to {len(self.push_db.keys())} unique repositories."
        commit_cmt = f"- Made commit comments to {len(self.commit_cmt_db.keys())} unique repositories."
        create = f"- Created {len(self.create_db.keys())} unique ref types."
        delete = f"- Deleted {len(self.delete_db.keys())} unique ref types."
        fork = f"- Forked {self.fork_db} unique repositories."
        nosupport = f"- These {len(self.not_supported)} events were not handled: {self.not_supported}"
        l = [push, commit_cmt, create, delete, fork, nosupport]
        output = "\n".join(l)
        return output
    
    def get_event_fn(self, key):
        event_fn_mappings = {
            "CommitCommentEvent": self.commit_comment_handler,
            "CreateEvent": self.create_handler,
            "DeleteEvent": self.delete_handler,
            "ForkEvent": self.fork_handler,
            "GollumEvent": None, #todo
            "IssueCommentEvent": None, #todo
            "IssuesEvent": None, #todo
            "MemberEvent": None, #todo
            "PublicEvent": None, #todo
            "PullRequestEvent": None, #todo
            "PullRequestReviewEvent": None, #todo
            "PullRequestReviewCommentEvent": None, #todo
            "PullRequestReviewThreadEvent": None, #todo
            "PushEvent": self.push_event_handler,
            "ReleaseEvent": None, #todo
            "SponsorshipEvent": None, #todo
            "WatchEvent": None, #todo
        }

        f = event_fn_mappings.get(key, None)
        if not f:
            self.not_supported.add(key)
        return f