// Import the express module
const express = require("express");
const AWS = require("aws-sdk");

AWS.config.update({ region: "us-west-1" });
const sqs = new AWS.SQS({ apiVersion: "2012-11-05" });
const queueUrl = "http://sqs:9324/000000000000/test-queue";

// Create an instance of express
const app = express();

// Use middleware to parse JSON bodies
app.use(express.json());

// Define a port number
const PORT = process.env.PORT || 3000;

// Define a /health route
app.get("/health", (req, res) => {
  res.status(200).json({ status: "OK" });
});

app.post("/", async (req, res) => {
  try {
    const { body } = req;
    console.log(req.body);

    if (!body) {
      return res.status(400).send("Body is mandatory");
    }

    console.log("Recieved message", body);

    const message = {
      MessageBody: JSON.stringify(body),
      QueueUrl: queueUrl
    };

    console.log("Putting message in queue", { message, queueUrl });

    const data = await sqs.sendMessage(message).promise();

    console.log("Message sent successfuly", message);

    return res.status(200).json(data);
  } catch (e) {
    console.error("Error send messages", error);
    return res.status(500).send("Error send messages");
  }
});

app.get("/fetch-events", async (req, res) => {
  const maxMessages = parseInt(req.query.max) || 10;

  const params = {
    QueueUrl: queueUrl,
    MaxNumberOfMessages: maxMessages
  };

  try {
    const data = await sqs.receiveMessage(params).promise();

    if (!data.Messages) {
      return res.status(200).json({ messages: [] });
    }

    // Handle deletion
    const deleteParams = {
      QueueUrl: queueUrl,
      Entries: data.Messages.map((message) => ({
        Id: message.MessageId,
        ReceiptHandle: message.ReceiptHandle
      }))
    };

    sqs.deleteMessageBatch(deleteParams).promise();

    return res.status(200).json({ messages: data.Messages.map(({ Body }) => JSON.parse(Body)) });
  } catch (error) {
    console.error("Error receiving messages", error);
    return res.status(500).send("Error receiving messages");
  }
});

// Start the server
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
