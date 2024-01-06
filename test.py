import awkward
import dask
import dask_awkward
import distributed
from distributed import Client
import uproot

if __name__ == "__main__":
    print("awkward.__version__", awkward.__version__)
    print("dask.__version__", dask.__version__)
    print("dask_awkward.__version__", dask_awkward.__version__)
    print("distributed.__version__", distributed.__version__)
    print("uproot.__version__", uproot.__version__)

    with Client() as _:
        events = uproot.dask("test.edm4hep.root:events",
                             filter_name="EcalEndcapNHits.energy")
        print(dask.compute(events["EcalEndcapNHits.energy"]))
