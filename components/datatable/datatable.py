from django_components import component

@component.register("datatable")
class Sidebar(component.Component):
    template_name = "datatable/template.html"
    
    def get_context_data(self):
        return {
            "headers": [
                {"name":"name","label":"Name"},
                {"name":"position","label":"Position"},
                {"name":"salary","label":"Salary"},
                {"name":"start_date","label":"Start Date"},
                {"name":"office","label":"Office"},
                {"name":"extn","label":"Extn"},
                ],
            "data":  [
                                            {
                                                "name": "Tiger Nixon",
                                                "position": "System Architect",
                                                "salary": "$320,800",
                                                "start_date": "2011/04/25",
                                                "office": "Edinburgh",
                                                "extn": "5421"
                                            },
                                            
                                         
                                          ],
        }