import glob
import os
import pandas as pd
import shutil


def main():
    # 엑셀 파일을 읽기
    try:
        # 두번째 시트 읽기        
        dt = pd.read_excel(r'D:/Python_vm/work/114_user.xlsx', sheet_name=1)        
        # dt = dt.dropna()

    except Exception as e:
        print("예외 발생 : ", e)

    # 첫인사 파일명을 filenames 에 리스트로 저장
    filenames_db = dt['file_nm_trs'].to_list()   

    # folder = r'Y:/agtment_new'
    folder = r'D:/Python_vm/work/agtment_new_bk'

    filenames_dir = os.listdir(f'{folder}')

    # 폴더 생성(없다면)
    dst_folder = f'{folder}/live'
    if not os.path.exists(dst_folder):
        os.makedirs(dst_folder)

    # os 폴더 리스트와 DB의 첫인사 파일 리스트를 비교
    # DB에 없는 파일은 삭제
    for filename in filenames_dir:
        if (not filename in filenames_db):
            # print(f'{folder}/{filename}')
            # os.remove(f'{folder}/{filename}')
            shutil.move(f'{folder}/{filename}', dst_folder)    

    # for file in file_nm:
    #     if (glob.glob(f'{folder}/{file}')):
    #     # print(f'{folder}/{file}')
    #     shutil.move(f'{folder}/{file}', dst_folder)


if __name__ == "__main__":
    main()