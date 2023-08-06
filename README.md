<!-- Project Overview -->
<div>
  <h1 align="center">Elastic create users and spaces</h1>

  <p align="center">
    Python script to create Elasticsearch users and Kibana spaces
    <br />
    <a href="https://sosaymon.github.io/elastic-create-users-and-spaces/"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/SoSaymon/elastic-create-users-and-spaces/issues">Report Bug</a>
    ·
    <a href="https://github.com/SoSaymon/elastic-create-users-and-spaces/issues">Request Feature</a>
  </p>
</div>

<!-- Table of Contents -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-project">About Project</a>
      <ul>
        <li><a href="#getting-started">Getting Started</a></li>
        <ul>
          <li><a href="#local-copy">Local copy</a></li>
            <ul>
              <li><a href="#prerequisites-lc">Prerequisites</a></li>
              <li><a href="#installation-lc">Installation</a></li>
              <li><a href="#configuration-lc">Configuration</a></li>
            </ul>
          <li><a href="#docker">Docker (Work In Progress)</a></li>
            <ul>
              <li><a href="#prerequisites-d">Prerequisites</a></li>
              <li><a href="#installation-d">Installation</a></li>
              <li><a href="#configuration-d">Configuration</a></li>
            </ul>
        </ul>
        <li><a href="#usage">Usage</a>
          <ul>
            <li><a href="#usage-lc">Local copy</a></li>
                <ul>
                  <li><a href="#create-space-lc">Create space</a></li>
                  <li><a href="#create-user-lc">Create user</a></li>
                </ul>
            <li><a href="#usage-d">Docker (Work In Progress)</a></li>
                <ul>
                  <li><a href="#create-space-d">Create space</a></li>
                  <li><a href="#create-user-d">Create user</a></li>
                </ul>
          </ul>
        </li>
      </ul>
    </li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>

<!-- About Project -->
<section>
    <div>
        <h1 id="about-project">About Project</h1>
        <img src="docs/images_readme/product-screenshot.png" alt="product screenshot">
        <p>
        This script is designed to create Elasticsearch users and Kibana spaces. The script is written in Python 3.11 and uses the Elasticsearch and Kibana APIs. The script, thanks to the possibility of loading CSV files, helps to shorten the process of adding users and spaces to a total minimum
        </p>
    </div>
    <div>
        <h2 id="getting-started">Getting Started</h2>
        <div>
            <h3 id="local-copy">Local copy</h3>
            <p>
            To get a local copy up and running follow these simple steps.
            </p>
            <h4 id="prerequisites-lc">Prerequisites</h4>
            <ol>
                <li>Python 3.11</li>
                <li>pip</li>
                <li>Url to your Elasticsearch and Kibana instance and Elastic admin username and password</li>
            </ol>
            <h4 id="installation-lc">Installation</h4>
            <ol>
                <li>
                    Clone the repo
                    <ul>
                        <li>
                            <code>
                                git clone https://github.com/SoSaymon/elastic-create-users-and-spaces.git
                            </code>
                        </li>
                    </ul>
                </li>
                <li>
                    Setup Virtual Environment
                <li>
                    Install Python packages
                    <ul>
                        <li><code>pip install -r requirements.txt</code></li>
                    </ul>
                </li>
            </ol>
            <h4 id="configuration-lc">Configuration</h4>
            <ol>
                <li>Rename file <code>.env_template</code> to <code>.env</code></li>
                <li>Fill in the variables in the <code>.env</code> file</li>
            </ol>
        </div>
        <div>
            <h3 id="docker">Docker</h3>
            <p>Docker image is not ready yet and is still under development</p>
        </div>
    </div>
    <div>
        <h2 id="usage">Usage</h2>
        <div>
            <h3 id="usage-lc">Local copy</h3>
            <div>
                <p id="create-space-lc">To create Kibana space follow these steps</p>
                <ol>
                    <li>
                        Enter this prompt in commandline<br/>
                        <code>python3 create.py space</code>
                    </li>
                    <li>
                        Follow the instructions in the prompt
                    </li>
                </ol>
                <p id="create-user-lc">To create Elasticsearch user follow these steps</p>
                <ol>
                    <li>
                        Enter this prompt in commandline<br/>
                        <code>python3 create.py user</code>
                    </li>
                    <li>
                        Follow the instructions in the prompt
                    </li>
                </ol>
            </div>
        </div>
    </div>
    <div>
        <h2 id="license">License</h2>
        <p>
            Distributed under the MIT License. See <a href="LICENSE">`LICENSE`</a> for more information.
        </p>
    </div>
    <div>
        <h2 id="contact">Contact</h2>
        <p>
            If you have any questions about the project, feel free to contact me at <a href="mailto:szymon.chirowski@protonmail.com">szymon.chirowski@protonmail.com</a>.<br/>
            You can find my other projects at <a href="https://github.com/SoSaymon/">My GitHub account</a>.
        </p>
        <p>
            Project Link: <a href="https://github.com/SoSaymon/elastic-create-users-and-spaces/">https://github.com/SoSaymon/elastic-create-users-and-spaces/</a><br/>
            Author: Szymon Chirowski <br/>
            Documentation: <a href="">LINK</a>
        </p>
    </div>
</section>
