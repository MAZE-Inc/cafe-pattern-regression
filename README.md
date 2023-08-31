# A-MAZE: 카페 현황 예측 AI
- 카페 내 현황을 분석해 생성한 빅데이터와 고객 UI/UX 빅데이터로 미래의 특성 예측하는 AI모델입니다.
- 모든 개별 카페와 고객에 대해 예측 모델을 훈련/검증하는 과정을 거쳤습니다.
- 자사의 카페 현황 예측 AI모델은 카페 내 좌석점유율 예측, 고객외형 예측, 행동 예측, 주문메뉴 및 매출 예측 총 4개의 예측을 수행합니다.
## 하드웨어 사양
| 품목 | 규격 |
|------|------|
|CPU|Intel CPU Core I9-10920X|
|M/B| ASUS WS X299 SAGE|
|RAM | Samsung DDR4 16GB PC4-25600|
|SSD|SK Hynix Gold P31 M.2 NVMe (1TB)|
|VGA|GFORCE RTX3080Ti D6X 12GB Ref X4|

## 소프트웨어 환경
Server : Ubuntu 20.04 x86_64  
Database : MongoDB

## 소프트웨어 환경 설치
### 개발에 필요한 기본 패키지 설치
```shell
$ sudo apt-get update
$ sudo apt-get upgrade
$ sudo apt-get install vim nano build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev wget gcc make python3-pip

```
### 그래픽카드 드라이버 설치
1. GPU와 호환되는 ubuntu diriver를 설치한다.
    ```shell 
    $ ubuntu-drivers devices
    ```
2. 설치 가능한 드라이버 리스트를 확인한다.
    ```shell 
    $ apt-cache search nvidia | grep nvidia-driver-{version}
    ```
3. 해당 저장소 추가하고, 패키지 매니저를 업데이트한다.
    ```shell 
    $ sudo add-apt-repository ppa:graphics-drivers/ppa
    $ sudo apt update
    ``` 
4. 해당 명령어로 설치된 드라이버를 확인한다.
    ```shell
    $ nvidia-smi
    ```

### CUDA 설치하기
1. cuda toolkit을 설치한다.  
    ###### CUDA toolkit 12.0.0 /Linux / x86_64 / Ubuntu20.04 기준
    ```shell
    $ wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/cuda-keyring_1.0-1_all.deb
    $ sudo dpkg -i cuda-keyring_1.0-1_all.deb
    $ sudo apt-get update
    $ sudo apt-get -y install cuda
    ```
    다른 환경에 대한 설치방법은 [해당 링크](https://developer.nvidia.com/cuda-12-0-0-download-archive) 참조할 것.

### CUDA 환경 설정
1. 아래 명령어로 설정파일을 연다.
    ```shell
    $ vim /etc/profile
    ```
2. 아래와 같은 명령어를 입력한다.
    ```shell
    $ export PATH=/usr/local/cuda-12.0/bin${PATH:+:${PATH}}
    $export LD_LIBRARY_PATH=/usr/local/cuda-12.0/lib64${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}
    $ export LD_LIBRARY_PATH=/usr/local/cuda-12.0/extras/CUPTI/lib64${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}
    ```
3. 설정 파일을 적용한다.
    ```shell
    $ source /etc/profile
    ```
#### cuDNN 설치하기  
1. [해당링크](https://developer.nvidia.com/rdp/cudnn-archive) 에서 CUDA 버전 및 서버 환경과 맞는 파일 다운로드 
2. 압축을 풀고 설치한다.
    ```shell
    $ unxz cudnn-linux-x86_64-8.7.0.84_cuda12-archive.tar.xz
    $ tar -xvf cudnn-linux-x86_64-8.7.0.84_cuda12-archive.tar

    $ sudo cp cudnn-linux-x86_64-8.7.0.84_cuda12-archive/include/* /usr/local/cuda-12/include
    $ sudo cp -P cudnn-linux-x86_64-8.7.0.84_cuda12-archive/lib/* /usr/local/cuda-12/lib64
    $ sudo chmod a+r /usr/local/cuda-12/lib64/libcudnn*

    $ cat /usr/local/cuda/include/cudnn_version.h | grep CUDNN_MAJOR -A 2
    ```

### Python 3.12 설치하기
```shell
$ tar -xvf Python-3.12.0a5.tar.xz
$ cd Python-3.12.0a5
$ ./configure --enable-optimizations
$ make -j 4
$ sudo make altinstall
$ sudo apt-get install python3-pip
```


#### Anaconda 설치하기 
1. [해당링크](https://repo.anaconda.com/archive/)에서 환경에 맞는 최신 버전을 다운로드한다.
    ```shell
    $ wget https://repo.anaconda.com/archive/Anaconda3-2023.07-2-Linux-x86_64.sh
    $ sudo bash Anaconda3-2021.05-Linux-x86_64.sh
    ```
2. Anaconda를 초기 설정을 활성화한다.
    ```shell
    $ source /usr/anaconda3/bin/activate 
    $ conda init
    $ source ~/.bashrc
    ```

### 기타 패키지 설치하기
아래 명령어를 통해 프로그램 실행에 필요한 파이썬 패키지 목록을 설치한다.
```shell
$ sudo pip3 install -r requirements.txt
```

## 실행
```shell
# model: act: 행동 추론, gender: 성별 추론, seat: 좌석 점유율 추론, menu: 메뉴 추론
# date: 년도, 월, 일, 시, 분, 초 순서
./run.bin --model act --date --2023-11-11-11-11-11
```
<img width="450" alt="스크린샷 2023-08-31 오후 10 09 15" src="https://github.com/MAZE-Inc/cafe-pattern-regression/assets/129044938/2df2fa63-f1b2-4e26-bfe5-26462391e90d">
<img width="450" alt="스크린샷 2023-08-31 오후 10 08 30" src="https://github.com/MAZE-Inc/cafe-pattern-regression/assets/129044938/5bccdb7e-2078-4ba7-ab4d-0d1c1aa95792">
<img width="450" alt="스크린샷 2023-08-31 오후 10 07 36" src="https://github.com/MAZE-Inc/cafe-pattern-regression/assets/129044938/ddbd43dc-9c34-482f-b976-8be7ec338efa">
<img width="450" alt="스크린샷 2023-08-31 오후 10 07 13" src="https://github.com/MAZE-Inc/cafe-pattern-regression/assets/129044938/c6aeb3fa-0c4d-4c8d-8d49-ec691da2b56b">


# 카페 현황 예측 4개의 모델
## 좌석 점유율 예측 모델
![카페 A 좌석 점유율 예측 그래프](https://github.com/MAZE-Inc/cafe-pattern-regression/assets/129044938/9a53d235-49db-42cc-b318-4cd1ce3c7691)
![카페 A 좌석 점유율 예측 그래프 (1)](https://github.com/MAZE-Inc/cafe-pattern-regression/assets/129044938/742e677a-9059-4b71-a1ed-fef94e26a0a9)


## 고객층 예측 모델
![카페 A 남성 비율 예측 그래프 (1)](https://github.com/MAZE-Inc/cafe-pattern-regression/assets/129044938/3e97b504-9ff4-4549-87e1-aee6b22f2b65)
![카페 A 남성 비율 예측 그래프](https://github.com/MAZE-Inc/cafe-pattern-regression/assets/129044938/84e68556-ebfb-43f4-96bf-8b6a58ec4e9d)

## 행동 패턴 예측 모델
![카페 A 행동 실제 그래프_](https://github.com/MAZE-Inc/cafe-pattern-regression/assets/129044938/6192db92-0370-48a2-b120-7d10e10d5ed3)
![카페 A 행동 예측 그래프_ (2)](https://github.com/MAZE-Inc/cafe-pattern-regression/assets/129044938/5d010faa-0a3a-49eb-9766-a8259c4e5901)

## 메뉴 예측 모델
![카페 A 메뉴 추론 그래프](https://github.com/MAZE-Inc/cafe-pattern-regression/assets/129044938/70ae8883-86bd-4a8b-bf19-bb4669ba0765)
![카페 A 메뉴 추론 그래프_](https://github.com/MAZE-Inc/cafe-pattern-regression/assets/129044938/508792bb-9779-4206-b5dc-877a79a1c7d6)
