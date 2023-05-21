import argparse
import parse
import pathlib



def parse_filename(file, filename_template: str):
    parsed = parse.parse(filename_template, file.name)
    return {
        'file': file,
        'order': int(parsed['num']),
        'ext': parsed['ext']
    }


def main():
    parser = argparse.ArgumentParser(description='Rename filenames to serial name')
    parser.add_argument('dirpath', help='source directory')
    parser.add_argument('filename_template', help='parse template (needs {num} and {ext})')
    parser.add_argument('--dry-run', help='print rename results only', action='store_true')
    args = parser.parse_args()
    dirpath = args.dirpath
    filename_template = args.filename_template
    dry_run = args.dry_run

    # 対象のファイルを取得
    files = pathlib.Path(dirpath).iterdir()

    # ファイル名をパースして順序、拡張子を抽出する
    file_info = (parse_filename(file, filename_template) for file in files)

    # 正しい順番にソート
    sorted_file_info = list(sorted(file_info, key=lambda x: x['order']))
    files_num = len(sorted_file_info)

    # 基数の計算
    base = 1
    while files_num >= 10:
        files_num = files_num // 10
        base += 1

    # ファイル名の変更
    for info in sorted_file_info:
        new_path = pathlib.Path(dirpath, f'IMG_{info["order"]:0{base}d}.{info["ext"]}')
        if dry_run:
            print(info['file'])
            print('-->', new_path)
            continue
        info['file'].rename(new_path)


if __name__ == '__main__':
    main()