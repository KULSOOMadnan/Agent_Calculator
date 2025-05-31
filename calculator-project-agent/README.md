<body>
  <div class="readme-container">
    <h1>Math God Agent</h1>
    <p class="subtitle">An advanced agentic calculator built with OpenAI Agents SDK</p>
    
    <div class="section">
      <h2>🔮 Project Overview</h2>
      <p>This project implements a powerful mathematical agent using OpenAI's Agents SDK with Gemini integration. The agent handles complex arithmetic operations through function tools while providing human-readable explanations.</p>
    </div>

    <div class="section">
      <h2>✨ Key Features</h2>
      <ul>
        <li><strong>8 Mathematical Operations</strong>: Addition, subtraction, multiplication, division, square, cube, square root, and exponentiation</li>
        <li><strong>Error Handling</strong>: Detects and prevents mathematical errors (division by zero, negative roots)</li>
        <li><strong>Step-by-Step Explanations</strong>: Provides reasoning behind calculations</li>
        <li><strong>Gemini Integration</strong>: Uses Google's Gemini 2.0 Flash model via OpenAI-compatible API</li>
        <li><strong>Interactive CLI</strong>: Conversational interface for natural math queries</li>
      </ul>
    </div>

    <div class="section">
      <h2>⚙️ Technical Implementation</h2>
      <h3>Core Components</h3>
      <pre><code>- Agent: Math God Agent (OpenAI Agents SDK)
- Model: Gemini 2.0 Flash (via OpenAI-compatible endpoint)
- Tools: 8 decorated mathematical functions
- Runner: Handles execution with RunConfig</code></pre>
      
      <h3>Architecture Flow</h3>
      <ol>
        <li>User input is received via CLI</li>
        <li>Agent determines if tool usage is required</li>
        <li>Selected tool executes the calculation</li>
        <li>Agent formats response with explanation</li>
        <li>Results are displayed to user</li>
      </ol>
    </div>

    <div class="section">
      <h2>🚀 Getting Started</h2>
      <h3>Prerequisites</h3>
      <pre><code>Python 3.9+
GEMINI_API_KEY in .env file
openai-agents package</code></pre>

      <h3>Installation</h3>
      <pre><code>pip install openai-agents python-dotenv</code></pre>

      <h3>Usage</h3>
      <pre><code>python math_agent.py</code></pre>
      <p>Sample queries:</p>
      <ul>
        <li>"What is 15 cubed?"</li>
        <li>"Calculate 5 divided by 0"</li>
        <li>"Find the square root of 144"</li>
      </ul>
    </div>

    <div class="section">
      <h2>🧠 Tool Functions</h2>
      <table>
        <tr>
          <th>Function</th>
          <th>Description</th>
          <th>Error Handling</th>
        </tr>
        <tr>
          <td>add(a, b)</td>
          <td>Sum of two numbers</td>
          <td>None</td>
        </tr>
        <tr>
          <td>divide(a, b)</td>
          <td>Division operation</td>
          <td>Prevents division by zero</td>
        </tr>
        <tr>
          <td>sqrt(n)</td>
          <td>Square root</td>
          <td>Prevents negative inputs</td>
        </tr>
        <!-- Other tools in similar rows -->
      </table>
    </div>

    <div class="section">
      <h2>📝 Code Highlights</h2>
      <h3>Agent Configuration</h3>
      <pre><code>agent = Agent(
    name="Math God Agent",
    instructions="Savage calculator with explanations...",
    tools=[add, subtract, multiply, ...],
    model=model
)</code></pre>

      <h3>RunConfig Setup</h3>
      <pre><code>config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)</code></pre>
    </div>

    <div class="section">
      <h2>📈 Future Enhancements</h2>
      <ul>
        <li>Add graphing capabilities</li>
        <li>Implement equation solving</li>
        <li>Add unit conversion tools</li>
        <li>Web interface version</li>
      </ul>
    </div>
  </div>

  <style>
    body {
      font-family: 'Segoe UI', sans-serif;
      line-height: 1.6;
      color: #333;
      max-width: 900px;
      margin: 0 auto;
      padding: 20px;
    }
    h1 {
      color: #2c3e50;
      border-bottom: 2px solid #3498db;
      padding-bottom: 10px;
    }
    .subtitle {
      font-style: italic;
      color: #7f8c8d;
    }
    .section {
      margin-bottom: 30px;
    }
    pre {
      background: #f8f9fa;
      padding: 15px;
      border-radius: 5px;
      overflow-x: auto;
    }
    table {
      width: 100%;
      border-collapse: collapse;
    }
    th, td {
      border: 1px solid #ddd;
      padding: 8px;
      text-align: left;
    }
    th {
      background-color: #f2f2f2;
    }
  </style>
</body>
