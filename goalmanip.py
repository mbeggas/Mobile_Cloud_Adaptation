import yaml
from rdflib import Graph

class GoalGraph (Graph):
    def __init__(self, ontology_url, context=None, precondition=None):
        super().__init__()
        self.load(ontology_url)
        print(context)
        print(precondition)
        with open("apifiles/contextprops.yaml", "r") as file:
            self.__contextprops = yaml.load(file, Loader=yaml.FullLoader)




if __name__ == "__main__":
    rdf_url = "https://raw.githubusercontent.com/mbeggas/Mobile_Cloud_Adaptation/master/ontologies/instaceonto.rdfs"
    goal = GoalGraph(rdf_url, precondition="aaa")