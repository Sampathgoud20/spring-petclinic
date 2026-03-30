FROM maven:eclipse-temurin:17-jdk-focal AS build
WORKDIR /app
COPY . /app
RUN mvn package -DskipTests

FROM eclipse-temurin:17-jre-alpine AS runtime
LABEL java project = SPC
WORKDIR /app
COPY --from=build /app/target/*.jar app.jar
EXPOSE 8080
CMD ["java", "-jar", "app.jar"]
