import os

class Middleware():

    def request_interceptor(self, header,scope):
        print("Middleware intercepting requests...")
        try:
            import local_settings
            key = local_settings.SECRET_AUTHORIZED_KEY
            value = local_settings.SECRET_AUTHORIZED_VALUE
        except:
            print("Please create a local_settings file")
            return True

        if "jobs" in str(scope):
            print("The request is coming from a Jobs scope")
            return True

        try:
            if str(header[key]) == value:
                print("The request is coming from an authorized caller")
                return True           
            else:
                print("The request is not coming from an authorized caller")
                return False
        except Exception as error:
            print("There was an error getting the authorized values")
            return False
        
        