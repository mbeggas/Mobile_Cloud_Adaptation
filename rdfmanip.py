import rdflib
from rdflib import Graph
from rdflib import URIRef, RDF, RDFS

#<class 'tuple'>: (rdflib.term.Variable('s'), rdflib.term.URIRef('http://www.w3.org/1999/02/22-rdf-syntax-ns#type'), rdflib.term.URIRef('https://raw.githubusercontent.com/mbeggas/Mobile_Cloud_Adaptation/master/ontologies/schemaonto.rdfs#Goal'))
def executeQuery(query, g):
    return g.query(query)


def getGoal(g):
    """query = 'select ?s	?v  where { ?s rdf:type or:RegleEevenement . ?s or:lancer ?v . ?s or:limiteMin ?lmin . ?s or:limiteMax ?lmax .  FILTER( xsd:integer(?lmin) <= '+str(x)+' && xsd:integer(?lmax) > '+str(x)+' ) . }'"""
    query = 'select ?s where { ?s rdf:type schm:Goal}'
    rows = g.query(query) #executeQuery(query, g)
    for row in rows:
        print(row.s)
        print(row.s.rsplit('#')[-1])


def askGoal0(g):
    query1 = """ 
    PREFIX  goal: <https://raw.githubusercontent.com/mbeggas/Mobile_Cloud_Adaptation/master/ontologies/goalonto#> 
    select ?p ?o 
        where{ 
            goal:maingoal ?p ?o
        } """

    query = """ 
    PREFIX  goal: <https://raw.githubusercontent.com/mbeggas/Mobile_Cloud_Adaptation/master/ontologies/goalonto#> 
    PREFIX schm: <https://raw.githubusercontent.com/mbeggas/Mobile_Cloud_Adaptation/master/ontologies/schemaonto.rdfs#>
    PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
    select  ?goalmin ?goalmax
    where{
        goal:maingoal schm:minImageSize ?goalmin ; 
                      schm:maxImageSize ?goalmax. 
        FILTER( xsd:decimal(?goalmin) <= 200  && xsd:decimal(?goalmax) >= 200 )
    } 
    """
    #

    print(query)
    rows = executeQuery(query, g)
    print(len(rows))
    for row in rows:
        print(row)


def askGoal1(g, size):
    query = 'ASK { '
    query += ' <file:///C:/Users/mbeggas/Google Drive/json-test/ontologies/instaceonto.rdfss#g1> go:minImageSize ?goalmin .'
    query += ' <file:///C:/Users/mbeggas/Google Drive/json-test/ontologies/instaceonto.rdfs#g1> go:maxImageSize ?goalmax .'
    query += '  FILTER(xsd:decimal(?goalmin) <= ' + str(size) + ' && xsd:decimal(?goalmax) >= ' + str(size) + ') .}'

    query = """ 
    PREFIX goal: <https://raw.githubusercontent.com/mbeggas/Mobile_Cloud_Adaptation/master/ontologies/goalonto#> 
    PREFIX schm: <https://raw.githubusercontent.com/mbeggas/Mobile_Cloud_Adaptation/master/ontologies/schemaonto.rdfs#>
    PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
    ASK{
        goal:maingoal schm:minImageSize ?goalmin ;
                      schm:maxImageSize ?goalmax  .
        FILTER( xsd:decimal(?goalmin) <= %s  && xsd:decimal(?goalmax) >= %s )  
        } """ % (size, size)

    query2 = """
    PREFIX  goal: <https://raw.githubusercontent.com/mbeggas/Mobile_Cloud_Adaptation/master/ontologies/goalonto#> 
    PREFIX schm: <https://raw.githubusercontent.com/mbeggas/Mobile_Cloud_Adaptation/master/ontologies/schemaonto.rdfs#>
    PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
    
    ask{
        goal:maingoal schm:minImageSize ?goalmin ; 
                      schm:maxImageSize ?goalmax. 
        FILTER( xsd:decimal(?goalmin) <= %s).
        FILTER(xsd:decimal(?goalmax) >= %s )
    } 
    """ % (size, size)



    #
    print(query2)
    # print(query)

    rows = executeQuery(query2, g)
    print(len(rows), rows.askAnswer)


def askGoal2(g, imageFormat):
    query = 'ASK where{ '
    query += ' <file:///C:/Users/othma/Desktop/dr/monir/InstancesGoal.rdfs#g1> go:ImageFormat ' + str(
        imageFormat) + ' .'
    query += ' }'

    query = """ 
    PREFIX goal: <https://raw.githubusercontent.com/mbeggas/Mobile_Cloud_Adaptation/master/ontologies/goalonto#> 
    PREFIX schm: <https://raw.githubusercontent.com/mbeggas/Mobile_Cloud_Adaptation/master/ontologies/schemaonto.rdfs#>
    PREFIX xsd:  <http://www.w3.org/2001/XMLSchema#>
    PREFIX inst: <https://raw.githubusercontent.com/mbeggas/Mobile_Cloud_Adaptation/master/ontologies/instaceonto.rdfs#>
    select ?s {
        goal:maingoal ?s inst:jpg .
        
        } """ # % (imageFormat)
    print(query)
    rows = executeQuery(query, g)
    print(len(rows), rows, rows.askAnswer)

    for r in rows:
        print(r)


if __name__ == '__main__':
    rdf_goal_graph = rdflib.Graph()
    goal_onto_url = "https://raw.githubusercontent.com/mbeggas/Mobile_Cloud_Adaptation/master/ontologies/goalonto" #'ontologies/instaceonto.rdfs'
    rdf_goal_graph.load(goal_onto_url)
    #getGoal(rdf_instances_graph)

    #askGoal0(rdf_goal_graph)
    #
    imageFormat = '<https://raw.githubusercontent.com/mbeggas/Mobile_Cloud_Adaptation/master/ontologies/instaceonto.rdfs#jpg>'
    size = 200
    #askGoal1(rdf_goal_graph, size)
    askGoal2(rdf_goal_graph, imageFormat)
    #
    # """for s,p,o in g:
    #     print s,p,o"""
