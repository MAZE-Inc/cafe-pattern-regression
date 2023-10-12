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
- 아래 모든 모델은 특정 카페 A에 대한 추론입니다.
### 메뉴 추론
<img src="./images/메뉴 추론 예시.png" width="450">

### 성별 추론
<img src="./images/성별 추론 예시.png" width="450">

### 좌석 점유율 추론
<img src="./images/좌석 점유율 추론 예시.png" width="450">

### 행동 추론
<img src="./images/행동 추론 예시.png" width="450">
 

# 카페 현황 예측 4개의 모델
## 모델 설명
자사 모델은 Boosting 모델을 기반으로 만들었습니다. Boosting모델은 여러 개의 약한 Decision Tree를 조합해서 사용하는 Ensemble 기법 중 하나입니다. 즉, 약한 예측 모형들의 학습 에러에 가중치를 두고, 순차적으로 다음 학습 모델에 반영하여 강한 예측모형을 만드는 것입니다.
<br />
모델 개념도는 아래의 그림과 같습니다. 
<br />
<img src="./images/부스팅 모델 개념도.png" width="450">
<br />  
y=m1(x)+error(x) 모델 m1이 x에 대해서 제대로 예측할 확률이 y라고 하고, 이 정확도를 높이려면
error(x)를 작게 하는 모델을 적용하면 되는데, error(x) = m2(x) + error2(x)라고 볼 수 있습니다. 마찬가지로 error(x)를 작게 하려면 error2(x)를 작게 하면 되는데, 그러기 위해서는 여기에 다른 모델을 적용하면 됩니다. 즉 error2(x) = m3(x)+error3(x)가 되고, 이를 식으로 합치면
y= m1(x)+m2(x)+m3(x)+error3(x)
가 됩니다. 이렇게 하면 m1,m2,m3 모델의 가중치가 같기 때문에, 서로 모델이 간섭을 하여, 좋은 결과를 내기 어렵다. 그래서, 각 모델에 가중치를 반영한다. 식은 y = W1m1(x)+W2m2(x)+W3m3(x)+error3(x)와 같은 식이 된다.
## 좌석 점유율 예측 모델
- 아래 그림은 자사의 좌석 점유율 예측 모델로 요일별, 시간별 예측을 시각화한 그림입니다.

<img src="./images/카페 A 좌석 점유율 예측 그래프.png" width="800">
<img src="./images/카페 A 좌석 점유율 예측 그래프2.png" width="800">

## 고객층 예측 모델
- 아래 그림은 자사의 고객층 예측 모델로 요일별, 시간별 예측을 시각화한 그림입니다.
<img src="./images/카페 A 남성 비율 예측 그래프.png" width="800">
<img src="./images/카페 A 남성 비율 예측 그래프2.png" width="800">

## 행동 패턴 예측 모델
- 아래 그림은 자사의 행동 패턴 예측 모델로 요일별, 시간별 예측을 시각화한 그림입니다.
<img src="./images/카페 A 행동 예측 그래프.png" width="800">
<img src="./images/카페 A 행동 예측 그래프2.png" width="800">

## 메뉴 예측 모델
- 아래 그림은 자사의 메뉴 예측 모델로 요일별, 시간별 예측을 시각화한 그림입니다.
<img src="./images/카페 A 메뉴 추론 그래프.png" width="800">
<img src="./images/카페 A 메뉴 추론 그래프2.png" width="800">

