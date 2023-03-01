from flask import Flask, request, jsonify, render_template
from neo4j import GraphDatabase
import json

app = Flask(__name__)
driver = GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "password"))  
// password为你的neo4j数据库密码

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/get_data', methods=['POST'])
def get_data():
    data = request.get_json()
    node_name = data['data']

    with driver.session() as session:
        result = session.run('MATCH (n {name: $name})-[r]-(m) RETURN n,r,m', name=node_name)

        nodes = []
        links = []
        node_ids = set()



        for record in result:
            node1 = record['n']
            node2 = record['m']
            link = record['r']

            nodes.append({
                "id": node1.element_id,
                "label": node1['name']
            })

            nodes.append({
                "id": node2.element_id,
                "label": node2['name']
            })

            links.append({
                "id": link.element_id,
                "from": node1.element_id,
                "to": node2.element_id,
                "label": link.type,
                "color":'black',
                "width":1
            })

            node_ids.add(node1.element_id)
            node_ids.add(node2.element_id)



       
    nodes = [dict(t) for t in {tuple(d.items()) for d in nodes}]

    print(json.dumps({"nodes": nodes, "links": links}))
    return json.dumps({"nodes": nodes, "links": links})


if __name__ == '__main__':
    app.run(debug=True)
