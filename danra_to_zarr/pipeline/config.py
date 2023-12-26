from pathlib import Path

FP_ROOT = Path("/dmidata/projects/cloudphysics/danra")


# A "data collection" may contain multiple named parts (each will be put in its own zarr archive)
# Each part may contain multiple "level types" (e.g. heightAboveGround, etc)
# and a name-mapping may also be defined


DATA_COLLECTIONS = {
    "v0.1.0": dict(
        description="first run of task for creating part of full dataset",
        rechunk_to=dict(time=4, x=512, y=512),
        timespan=slice("2015-01-01", "2015-02-01"),
        parts=dict(
            height_levels=dict(
                heightAboveGround=dict(variables={v: [100] for v in "t r u v".split()})
            ),
            pressure_levels=dict(
                isobaricInhPa=dict(
                    variables={v: [1000] for v in "z t u v tw r ciwc cwat".split()}
                )
            ),
            single_levels=dict(
                heightAboveGround=dict(
                    variables={
                        **{
                            v: [0]
                            for v in [
                                "hcc",
                                "icei",
                                "lcc",
                                "lwavr",
                                "mcc",
                                "mld",
                                "pres",
                                "prtp",
                                "psct",
                                "pscw",
                                "pstb",
                                "pstbc",
                                "sf",
                                "swavr",
                                "vis",
                                "xhail",
                                # TODO: `rain`, `snow`, `snsub`, `nlwrs`, `nswrs`, `lhsub`,
                                # `lhe`, `grpl`, `dni`, `grad`, `sshf`, `wevap`, `vflx`, `uflx`, `tp`
                                # use time-range indicator 4, but dmidc currently assumes 0
                                # "rain",
                                # "snow",
                                # "snsub",
                                # "nlwrs",
                                # "nswrs",
                                # "lhsub",
                                # "lhe",
                                # "grpl",
                                # "dni",
                                # "grad",
                                # "sshf",
                                # "wevap",
                                # "vflx",
                                # "uflx",
                                # "tp",
                            ]
                        },
                        **{
                            "t": [0, 2],
                            # TODO: `tmin` and `tmax` use time-range indicator 2, but dmidc currently assumes 0
                            # "tmin": [2],
                            # "tmax": [2],
                            "r": [2],
                            "u": [10],
                            "v": [10],
                            # TODO: in next version add ugst and vgst, but dmidc needs to be updated first
                            # to change timerange_indicator to 10 (rather than 0 by default), need to find
                            # out what value 10 means too..
                            # "ugst": [10],
                            # "vgst": [10],
                        },
                    },
                    name_mapping="{var_name}{level}m",
                ),
                entireAtmosphere=dict(
                    variables={v: [0] for v in "pwat cape cb ct grpl".split()},
                    name_mapping="column_{var_name}",
                ),
                nominalTop=dict(
                    variables=dict(nswrt=[0], nlwrt=[0]), name_mapping="{var_name}_toa"
                ),
                heightAboveSea=dict(
                    variables=dict(pres=[0]), name_mapping="{var_name}_seasurface"
                ),
            ),
        ),
    ),
    "v0.2.0": dict(
        timespan=slice("2015-01-01", "2016-01-01"),
        parts=dict(
            height_levels=dict(
                heightAboveGround=dict(
                    variables={
                        v: [30, 50, 75, 100, 150, 200, 250, 300, 500]
                        for v in "t r u v".split()
                    }
                )
            ),
            pressure_levels=dict(
                isobaricInhPa=dict(
                    variables={
                        v: [
                            100,
                            200,
                            250,
                            300,
                            400,
                            500,
                            600,
                            700,
                            800,
                            850,
                            900,
                            925,
                            950,
                            1000,
                        ]
                        for v in "z t u v tw r ciwc cwat".split()
                    }
                )
            ),
            single_levels=dict(
                heightAboveGround=dict(
                    variables={
                        **{
                            v: [0]
                            for v in [
                                "hcc",
                                "icei",
                                "lcc",
                                "lwavr",
                                "mcc",
                                "mld",
                                "pres",
                                "prtp",
                                "psct",
                                "pscw",
                                "pstb",
                                "pstbc",
                                "sf",
                                "swavr",
                                "vis",
                                "xhail",
                                # TODO: `rain`, `snow`, `snsub`, `nlwrs`, `nswrs`, `lhsub`,
                                # `lhe`, `grpl`, `dni`, `grad`, `sshf`, `wevap`, `vflx`, `uflx`, `tp`
                                # use time-range indicator 4, but dmidc currently assumes 0
                                # "rain",
                                # "snow",
                                # "snsub",
                                # "nlwrs",
                                # "nswrs",
                                # "lhsub",
                                # "lhe",
                                # "grpl",
                                # "dni",
                                # "grad",
                                # "sshf",
                                # "wevap",
                                # "vflx",
                                # "uflx",
                                # "tp",
                            ]
                        },
                        **{
                            "t": [0, 2],
                            # TODO: `tmin` and `tmax` use time-range indicator 2, but dmidc currently assumes 0
                            # "tmin": [2],
                            # "tmax": [2],
                            "r": [2],
                            "u": [10],
                            "v": [10],
                            # TODO: in next version add ugst and vgst, but dmidc needs to be updated first
                            # to change timerange_indicator to 10 (rather than 0 by default), need to find
                            # out what value 10 means too..
                            # "ugst": [10],
                            # "vgst": [10],
                        },
                    },
                    name_mapping="{var_name}{level}m",
                ),
                entireAtmosphere=dict(
                    variables={v: [0] for v in "pwat cape cb ct grpl".split()},
                    name_mapping="column_{var_name}",
                ),
                nominalTop=dict(
                    variables=dict(nswrt=[0], nlwrt=[0]), name_mapping="{var_name}_toa"
                ),
                heightAboveSea=dict(
                    variables=dict(pres=[0]), name_mapping="{var_name}_seasurface"
                ),
            ),
        ),
    ),
}