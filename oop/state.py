


class Pull:

    def __init__(self, state, name):
        self.name = name
        self.change_state(state)

    def change_state(self, state):
        print(f"Context of {self.name} changing to {type(state).__name__}")
        self.state = state
        self.state.context = self

    def check_success(self):
        print(f"approved on state {type(self.state).__name__}")
        self.state.passed()

    def check_failed(self):
        print(f"disapproved on state {type(self.state).__name__}")
        self.state.failed()


class StateInDevelopment:

    def passed(self):
        self.context.change_state(StateInReview())

    def failed(self):
        self.context.change_state(StateInDevelopment())


class StateApproved:

    def passed(self):
        pass

    def failed(self):
        pass


class StateInReview:

    def passed(self):
        self.context.change_state(StateApproved())

    def failed(self):
        self.context.change_state(StateInDevelopment())


if __name__ == '__main__':
    my_pull_request = Pull(StateInDevelopment(), '1 pull request')
    my_pull_request.check_success()
    my_pull_request.check_success()
    my_next_pull_request = Pull(StateInDevelopment(), '2 pull request')
    my_next_pull_request.check_failed()
    my_next_pull_request.check_success()
    my_next_pull_request.check_failed()
