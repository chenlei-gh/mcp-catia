# 建模历史与撤销/重做、回放
class HistoryFeature:
    def __init__(self, service):
        self.service = service
        self.history = []
        self.redo_stack = []

    def record(self, action: str, params: dict):
        self.history.append((action, params))
        self.redo_stack.clear()

    def undo(self):
        if not self.history:
            return 'fail: no history'
        last = self.history.pop()
        self.redo_stack.append(last)
        # 伪代码：实际应回滚CATIA模型到上一步
        return 'ok'

    def redo(self):
        if not self.redo_stack:
            return 'fail: no redo'
        action, params = self.redo_stack.pop()
        # 伪代码：实际应重做该操作
        self.history.append((action, params))
        return 'ok'

    def get_history(self):
        return self.history
