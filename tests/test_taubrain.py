
import taubrain as tb 

def test_tortusity_geometric_value_zero():
    assert tb.tortuosity.tortuosity_geometric_track([]) == 0


#            __
#           / _)
#    .-^^^-/ /
# __/       /
# <__.|_|-|_| -> octajos