from Engine.loader import load_ltf
from Engine.htfbuilder import build_htf
from IctCoreEngine.context import build_core_context

def build_context(pair):
    ltf = load_ltf(pair)
    htf = build_htf(ltf, tf=15)
    
    return build_core_context(ltf, htf)
