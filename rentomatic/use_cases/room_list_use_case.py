from rentomatic.response_objects import response_objects as res


class RoomListUseCase:

    def __init__(self, repo):
        self.repo = repo

    def execute(self, request_obj):
        if not request_obj:
            return res.ResponseFailure.build_from_invalid_request_object(request_obj)
        try:
            rooms = self.repo.list(filters=request_obj.filters)
            return res.ResponseSuccess(rooms)
        except Exception as e:
            return res.ResponseFailure.build_system_error(
                "{}: {}".format(e.__class__.__name__, "{}".format(e)))
