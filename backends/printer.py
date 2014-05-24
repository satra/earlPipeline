# An example dummy backend, which implements the backend API and prints the
# underlying graph structure.

# Pipeline object
class Pipeline:
    def __init__(self, name):
        self.name = name
        self.type = 'PrinterPipeline'
        self.units = []
        self.edges = []

    def run(self):
        graph = "Units: " + str(self.units) + "\nEdges: " + str(self.edges)
        return graph

    def get_unit(self, name):
        return filter(lambda u: u.name == name, self.units)[0]

    def add_unit(self, unit, unit_name):
        unit.name = unit_name
        self.units.append(unit)

    def remove_unit(self, name):
        unit = self.get_unit(name)
        self.units.remove(unit)

    def get_port_string(self, src_name, src_port, dst_name, dst_port):
        return self.edges.append(src_name + "." + src_port + "->" + dst_name + "." + dst_port)

    def connect(self, src_name, src_port, dst_name, dst_port):
        edge = Edge(src_name, src_port, dst_name, dst_port)
        self.edges.append(edge)
        return edge

    def disconnect(self, src_name, src_port, dst_name, dst_port):
        obj = filter(lambda edge:
                edge.src == src_name and
                edge.srcPort == src_port and
                edge.dst == dst_name and
                edge.dstPort == dst_port, self.edges)[0]
        self.edges.remove(obj)

# Edge object
class Edge(object):
    def __init__(self, src, srcPort, dst, dstPort):
        self.src = src
        self.srcPort = srcPort
        self.dst = dst
        self.dstPort = dstPort

    def _get_id(self):
        return self.src+"."+self.srcPort+"->"+self.dst+"."+self.dstPort

    id = property(_get_id)


# Available unit types
class ONode:
    in_ports = []
    out_ports = ['out1', 'out2']

class IONode:
    in_ports = ['in1']
    out_ports = ['out1']

class INode:
    in_ports = ['in1', 'in2']
    out_ports = []

# method, returning types
def get_unit_types():
    return [ONode, IONode, INode]
    


