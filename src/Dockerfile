FROM python:3.4-alpine3.7

RUN addgroup -S myapp && adduser -S -G myapp myapp \
	&& mkdir /data \
	&& chown myapp:myapp /data


RUN apk add --no-cache pcre libpq libuuid openssh-client
RUN apk add --no-cache --virtual .build-deps  \
		bzip2-dev \
		coreutils \
		dpkg-dev dpkg \
		expat-dev \
		gcc \
		gdbm-dev \
		libc-dev \
		libffi-dev \
		libnsl-dev \
		openssl \
		libtirpc-dev \
		linux-headers \
		make \
		ncurses-dev \
		pax-utils \
		readline-dev \
		sqlite-dev \
		tcl-dev \
		tk \
		tk-dev \
		xz-dev \
		zlib-dev \
		pcre-dev \
		postgresql-dev \
        && pip install --upgrade pip \
        && pip install uwsgi \
		&& pip install psycopg2 \
		&& pip install pysftp \
	&& apk del .build-deps

ADD --chown=myapp:myapp app/ /app
WORKDIR /app

CMD [ "uwsgi", "--thunder-lock", "--ini", "/app/uwsgi.ini"]
