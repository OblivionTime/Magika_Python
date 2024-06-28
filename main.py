# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import json
import subprocess
import sys

from magika import Magika, PredictionMode, MagikaError
import colors
from pathlib import Path


def main(filePath):
    p = Path(filePath)
    # 判断文件是否存在
    if not p.exists():
        print(f'File or directory "{str(p)}" does not exist.')
        sys.exit(1)
    # 初始化magika
    prediction_mode_str = "high-confidence"

    try:
        magika = Magika(
            model_dir=None,
            prediction_mode=PredictionMode(prediction_mode_str),
            no_dereference=False,
            verbose=False,
            debug=False,
            use_colors=True,
        )
    except MagikaError as mr:
        print(str(mr))
        sys.exit(1)
    oriExt = p.suffix
    if len(oriExt) > 0:
        oriExt = oriExt[1:]
    magika_result = magika.identify_path(p)
    output_extensions = magika_result.output.extensions
    realExt = magika_result.output.group
    if (oriExt != "" and oriExt.lower() in output_extensions):
        realExt = oriExt
    print(json.dumps({
        "oriExt": oriExt,
        "realExt": realExt
    }, indent=4))


if __name__ == '__main__':
    if len(sys.argv)!=2:
        print("参数错误")
        sys.exit(1)
    filePath=sys.argv[1]
    main(filePath)
