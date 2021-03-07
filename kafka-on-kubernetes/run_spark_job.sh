#!/bin/bash

# How to configure ENVIRONMENT VARIABLE?
cd /home/hadoop/Video-Stream-Analytics-Using-OpenCV-Kafka-and-Spark-Technologies/kafka-on-kubernetes

# Clean yarn application before start
clear_yarn_application() {
  for x in $(yarn application -list -appTypes SPARK | awk 'NR > 2 { print $1 }'); do
    yarn application -kill $x
  done
}

zip_py_files_for_spark_jobs() {
  zip \
  py-files.zip \
  VideoProcessor.py
}

# spark-submit options
# --py-files: pyspark를 사용할 때 module path로 사용하게 되는 파일들이 들어가는 것들을 모음
#             중요한 것은, .py 파일 같은 것들'만' 들어가서 사용하게 된다는 점.
#             만약 여기에 패키지를 깔고 싶으면
#             pip3 install <packages> -t <특정 directory>j
#             zip <name>.zip <특정 directory>
# --files: 일반적인 spark에서 사용되는 yaml, txt등 일반적인 파일을 공유해서 사용할 수 있도록 하는 옵션
#          해당 옵션은 hdfs에 공유되어 찾을 수 있도록 설정 됨.
#          현재 상황에서는 config.yaml 파일을 공유하기 위해 옵션을 지정해주고 자동으로 hdfs를 참조해서 찾아오게 됨.
#          참고: config.yaml -> resource { scheme: "hdfs" host: "ip-172-31-11-7.ap-northeast-2.compute.internal" port: 8020 file: "/user/root/.sparkStaging/application_1592795466100_0266/config.yaml" }

submit_spark_jobs() {
    echo "Spark Jobs are running."
    echo "GAUA!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
    spark-submit \
      --master yarn \
      --deploy-mode cluster \
      --packages org.apache.spark:spark-sql-kafka-0-10_2.12:2.4.6 \
      --py-files py-files.zip \
      VideoProcessor.py
    echo "Spark Jobs are done."
}

zip_py_files_for_spark_jobs
submit_spark_jobs
