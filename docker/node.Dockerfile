# pull official base image
FROM node:latest

# set working directory
WORKDIR /app

RUN apt-get update -y
RUN apt-get install libgtk2.0-0 libgtk-3-0 libgbm-dev libnotify-dev libgconf-2-4 libnss3 libxss1 libasound2 libxtst6 xauth xvfb -y

# add `/app/node_modules/.bin` to $PATH
ENV PATH /app/node_modules/.bin:$PATH

# install app dependencies
COPY ./web/package.json ./
COPY ./web/package-lock.json ./
RUN npm install
RUN npm install react-scripts@3.4.1 -g

# add app
COPY ./web/ ./

# start app
CMD ["next", "dev"]