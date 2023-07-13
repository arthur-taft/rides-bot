from flask import Flask, Response, request

from rides_bot import run_bot


class UpdateArgs(object):

    def __init__(self, arg_dict):
        for arg, val in arg_dict.items():
            self.__setattr__(f'{arg}', val)


# Handle the groupme callback
callback = Flask('callback')


@callback.post('/update')
def groupme():
    data = request.get_json()
    update_args = {
        'debug': True,
        'groupme': False,
        'date': False,
        'gm_debug': False,
        'login': False,
        'message': False,
    }
    if data.__getitem__('text') == 'refresh':
        run_bot(UpdateArgs(update_args))
        return Response(status=200)
    else:
        return Response(status=204)


if __name__ == '__main__':
    callback.run(host='0.0.0.0', port=7045, debug=True)