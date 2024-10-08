# Use Node.js LTS version image
FROM node:lts

# Set the working directory
WORKDIR /app

# Copy package.json and package-lock.json
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the rest of the code into the container
COPY . .

# Expose port 5000 for HTTP server
EXPOSE 5000

# Run the service2.js when the container starts
CMD ["node", "service2.js"]
