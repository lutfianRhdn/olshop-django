from django_components import component

@component.register("sidebar")
class Sidebar(component.Component):
    template_name = "sidebar/template.html"
    
    def get_context_data(self):
        return {"navitems":[
          {
            "root": "Navigation",
            "childs":[
              {"name": "Products", 'url': "/products",'icon': "fa fa-square"},
              {"name": "Categories", 'url': "/categories",'icon': "fa fa-list"},
              {"name": "Order", 'url': "/orders",'icon': "fa fa-cart"},
              
            ]
           },
        ]}