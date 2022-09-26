from byteflow2 import ByteFlow, ByteFlowRenderer
from simulator import Simulator
from pprint import pprint


def foo(x):
    c = 0
    for i in range(x):
        c += i
        if i == 100:
            break
    return c


def test_foo():
    flow = ByteFlow.from_bytecode(foo)
    pprint(flow.bbmap)
    flow = flow.restructure()
    pprint(flow.bbmap)
    # pprint(rtsflow.bbmap)
    ByteFlowRenderer().render_byteflow(flow).view()

    sim = Simulator(flow, foo.__globals__)
    ret = sim.run(dict(x=0))
    assert ret == foo(x=0)

    sim = Simulator(flow, foo.__globals__)
    ret = sim.run(dict(x=100))
    assert ret == foo(x=100)

if __name__ == "__main__":
    test_foo()
