import yaml
from rdflib import Graph


class GoalGraph(Graph):
    def __init__(self, ontology_url, context=None, precondition=None):
        super().__init__()
        self.load(ontology_url)
        print(context)
        print(precondition)
        # TODO generate Goal by set of rdf predicate form context or from precondition
        if context:
            self.__add_goal_from_context(context)

        if precondition:
            self.__add_goal_from_precondition(precondition)

    def __add_goal_from_context(self, context):
        with open("apifiles/contextprops.yaml", "r") as file:
            self.__contextprops = yaml.load(file, Loader=yaml.FullLoader)

    def __add_goal_from_precondition(self, precondition):
        pass

    def execute_ask_query(self, ask_query):
        pass


if __name__ == "__main__":
    rdf_url = "https://raw.githubusercontent.com/mbeggas/Mobile_Cloud_Adaptation/master/ontologies/instaceonto.rdfs"
    goal = GoalGraph(rdf_url, precondition="aaa")
