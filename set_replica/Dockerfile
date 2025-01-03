FROM mongo:4.4.0

# Copy the script into the image
COPY set-replica.sh /usr/local/bin/set-replica.sh
# Make the script executable
RUN chmod +x /usr/local/bin/set-replica.sh

CMD ["/usr/local/bin/set-replica.sh"]