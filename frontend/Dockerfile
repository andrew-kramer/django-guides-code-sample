# This image is *only* used in the development configuration, because that is the only configuration where we need
# real-time updates to the frontend. In testing / production, we use a static build of the frontend.
#
# Because we use a mounted volume, we don't need to copy all our files onto this image

# Starting image
FROM node:17-alpine3.12

# Set environment variables
ENV APP_HOME=/home/app/frontend
ENV NODE_OPTIONS=--openssl-legacy-provider

# Create the working directory
RUN mkdir -p $APP_HOME

# Create the "app" user
RUN addgroup -S app \
    && adduser -S -D -s /sbin/nologin -h /home/app -G app app

# Change ownership to "app" user
RUN chown -R app:app /home/app

# Set as the working directory
WORKDIR $APP_HOME

# Copy all files to the working directory
# DEV: Don't run this (see above)
# COPY --chown=app:app * .

# Make entrypoint.sh executable
# DEV: Don't run this (see above)
# RUN chmod 0744 entrypoint.sh

# Set current user to "app" user
USER app:app

# Install frontend dependencies
# DEV: Don't run this (see above)
# RUN npm install

# Set application entrypoint
ENTRYPOINT [ "/home/app/frontend/entrypoint.sh" ]