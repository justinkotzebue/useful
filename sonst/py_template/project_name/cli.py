import click
from yamlconfig.click_option import yaml_config_option
logger = logging.getLogger(__name__)


@click.group()
def cli():
    """Cloud Masking for S2 and L8"""
    pass


@cli.command()
@click.option('--path_input', '-i', required=True, help='path to unzipped ".SAFE" folder',
            type=click.Path(dir_okay=True))
@click.option('--skip_already_processed',
            help='If False, the final cloud mask product will be reprocessed',
            is_flag=False)
@click.option('--debug', default=False, help='Show debug information')
@yaml_config_option()
def s2(debug, **kwargs):
    """Create cloud masks for Sentinel 2"""
    from . import workflow as wf
    from . import logs
    logs.set_cli_logger(debug=debug)
    wf.loop_cm_s2(**kwargs)


@cli.command()
@click.option('--path_input', required=True, help='path to unzipped Landsat scence folder',
            type=click.Path(dir_okay=True))
@click.option('--aoi_type', required=True,
            help='Choose the Area of interest type which is used by idepix Neural Network classification, default = "ALL" ["ALL","LAND","LAND_USE_THERMAL","WATER","WATER_NOTIDAL","WATER_USE_THERMAL","WATER_NOTIDAL_USE_THERMAL"]',
            type=click.Choice(["ALL","LAND","LAND_USE_THERMAL","WATER",
                            "WATER_NOTIDAL","WATER_USE_THERMAL",
                            "WATER_NOTIDAL_USE_THERMAL"]), default="ALL")
@click.option('--skip_already_processed',
            required=False, help='If False, the final cloud mask product will be reprocessed',
            type=click.BOOL, default=True)
@yaml_config_option()
def l8(**kwargs):
    """
    Cloud Mask for Landsat
    """
    from . import workflow as wf
    wf.loop_cm_l8(**kwargs)
