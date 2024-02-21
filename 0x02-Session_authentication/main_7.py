#!/usr/bin/python3
""" Check response
"""

if __name__ == "__main__":
    try:
        from api.v1.auth.session_exp_auth import SessionExpAuth
        sea = SessionExpAuth()
        session_id = None
        user_id = sea.user_id_for_session_id(session_id)
        if user_id is not None:
            print("user_id_for_session_id should return None if session_id is None")
            exit(1)
        
        print("OK", end="")
    except:
        import sys
        print("Error: {}".format(sys.exc_info()))
