from IctCoreEngine.bias import htf_bias
from IctCoreEngine.liquidity import liquidity_sweep
from IctCoreEngine.structure import detect_market_structure
from IctCoreEngine.imbalance import find_fvg
from IctCoreEngine.orderblock import find_orderblock
from IctCoreEngine.sessions import session_context

def build_core_context(ltf, htf):
    """
    ltf : List[Dict] -> M1 candles (from Data/)
    htf : List[Dict] -> HTF candles (from Data/)
    """

    ctx = {}

    # 1️ Higher timeframe narrative
    ctx["bias"] = htf_bias(htf)

    # 2️ Liquidity raid
    ctx["liquidity"] = liquidity_sweep(ltf)

    # 3️ Institutional market structure
    ctx["structure"] = detect_market_structure(
        ltf=ltf,
        bias=ctx["bias"],
        liquidity=ctx["liquidity"]
    )

    # 4️ Displacement / imbalance
    ctx["fvg"] = find_fvg(ltf)

    # 5️ Order block aligned with structure
    ctx["orderblock"] = find_orderblock(
        ltf=ltf,
        bias=ctx["bias"],
        structure=ctx["structure"]
    )

    # 6️ Time filter
    ctx["session"] = session_context()

    return ctx
