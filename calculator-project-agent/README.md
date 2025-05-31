<body>
    <h1>Math God Agent 🧮✨</h1>
    <p>Meet the <strong>Math God Agent</strong> — a powerful calculator built with the <code>agents</code> library, using tool calling to crush arithmetic operations! From basic addition to complex square roots and powers, this agent delivers precise results with step-by-step explanations. 🚀</p>

    <h2>Features 🌟</h2>
    <ul>
        <li>➕ <strong>Arithmetic Operations</strong>: Addition, subtraction, multiplication, and division.</li>
        <li>🔢 <strong>Advanced Calculations</strong>: Squares, cubes, square roots, and arbitrary powers.</li>
        <li>💬 <strong>Interactive Interface</strong>: Command-line input for seamless user interaction.</li>
        <li>🛠️ <strong>Tool Calling</strong>: Smartly invokes functions for accurate calculations.</li>
        <li>📝 <strong>Step-by-Step Explanations</strong>: Explains results in simple, nerd-friendly language.</li>
    </ul>

    <h2>Setup 🛠️</h2>
    <ol>
        <li><strong>Install Python</strong> 🐍: Ensure Python 3.8+ is installed.</li>
        <li><strong>Install Dependencies</strong> 📦: Install required packages using pip:
            <pre><code>pip install agents python-dotenv openai</code></pre>
        </li>
        <li><strong>Set Up Environment</strong> 🔑: Create a <code>.env</code> file in the project root with your Gemini API key:
            <pre><code>GEMINI_API_KEY=your-gemini-api-key</code></pre>
            Alternatively, use an OpenAI API key for better tool-calling support:
            <pre><code>OPENAI_API_KEY=your-openai-api-key</code></pre>
        </li>
        <li><strong>Download the Code</strong> 💾: Save the Python script (e.g., <code>math_god_agent.py</code>) in your project directory.</li>
    </ol>

    <h2>Usage 🎮</h2>
    <p>Run the script to unleash the Math God Agent:</p>
    <pre><code>python math_god_agent.py</code></pre>
    <p>Interact with the agent by entering queries like:</p>
    <ul>
        <li>➕ <code>What is the sum of 5 and 10?</code></li>
        <li>√ <code>Calculate the square root of 16.</code></li>
        <li>🔋 <code>What is 2 raised to the power of 3?</code></li>
    </ul>
    <p>Type <code>exit</code> to quit with a sassy “Bye bye nerd 🤓”.</p>

    <h2>Code Structure 🏗️</h2>
    <ul>
        <li>🤖 <strong>Agent Setup</strong>: Creates the <code>Math God Agent</code> with instructions and arithmetic tools.</li>
        <li>🛠️ <strong>Tools</strong>: Async functions (<code>add</code>, <code>subtract</code>, <code>multiply</code>, <code>divide</code>, <code>square</code>, <code>cube</code>, <code>sqrt</code>, <code>power</code>) decorated with <code>@function_tool</code>.</li>
        <li>⚙️ <strong>Configuration</strong>: Uses <code>RunConfig</code> with an <code>OpenAIChatCompletionsModel</code> and a Gemini API client (or OpenAI client).</li>
        <li>🔄 <strong>Interactive Loop</strong>: Continuously processes user queries with <code>Runner.run</code>.</li>
    </ul>

    <h2>Notes 📌</h2>
    <ul>
        <li>⚠️ <strong>Gemini API Compatibility</strong>: The code uses the Gemini API’s OpenAI-compatible endpoint. Tool calling may not be fully supported. If errors occur, switch to OpenAI’s API:
            <pre><code>from openai import AsyncOpenAI
external_client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))
model = OpenAIChatCompletionsModel(model="gpt-4o-mini", openai_client=external_client)</code></pre>
        </li>
        <li>🚩 <strong>Model Provider Issue</strong>: The <code>model_provider</code> in <code>RunConfig</code> may require a custom <code>ModelProvider</code> class to avoid type errors. See the code for details.</li>
        <li>🔍 <strong>Model ID</strong>: Verify <code>gemini-2.0-flash</code> is valid. Use <code>gemini-1.5-flash</code> or <code>gemini-1.5-pro</code> if needed (check <a href="https://ai.google.dev/gemini-api/docs/openai">Gemini API docs</a>).</li>
    </ul>

    <h2>Example Queries and Outputs 📊</h2>
    <ul>
        <li><strong>Query</strong> ➕: <code>What is the sum of 5 and 10?</code><br>
            <strong>Output</strong>: The sum of 5 and 10 is 15.</li>
        <li><strong>Query</strong> 🔋: <code>Calculate 3 to the power of 4.</code><br>
            <strong>Output</strong>: 3 raised to the power of 4 is 81.</li>
        <li><strong>Query</strong> √: <code>What is the square root of 25?</code><br>
            <strong>Output</strong>: The square root of 25 is 5.</li>
    </ul>
</body>
