class Router:
    
    def __init__(self, modules):
        self.modules = modules

    def handle(self, query, user_id):
        
        for module in self.modules:
            
            if module.can_handle(query):
                return module.execute(query=query, user_id=user_id)
        
        return {"status": "error", "message": "No module found"}