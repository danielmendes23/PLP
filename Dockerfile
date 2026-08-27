FROM eclipse-temurin:17-jre

RUN apt-get update && apt-get install -y wget && rm -rf /var/lib/apt/lists/*

RUN wget -O /opt/jython.jar "https://repo1.maven.org/maven2/org/python/jython-standalone/2.7.4/jython-standalone-2.7.4.jar"

WORKDIR /app

COPY exemplo1.py /app/
COPY exemplo2.py /app/

ENTRYPOINT ["java", "-Dfile.encoding=UTF-8", "--enable-native-access=ALL-UNNAMED", "-jar", "/opt/jython.jar"]

CMD ["exemplo1.py"]