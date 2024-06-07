from django_components import component

@component.register("datatable")
class Sidebar(component.Component):
    template_name = "datatable/template.html"
    
    # def get_context_data(self):
    #     return 