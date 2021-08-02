#GHTracker setup

1. Fork [this repository](https://github.com/HID-GS/ghtracker/)
2. Create a [personal access token](https://github.com/settings/tokens)
3. Copy the _example.config.yaml_ file to _config.yaml_
4. On [your own repo](https://github.com/YOUR-ORG/ghtracker/settings/secrets/actions), create a secret called _GHCONFIG_
5. Populate the _GHCONFIG_ secret with the base64 content of your own _config.yaml_ file

After this, the workflow should run every night. Your elastic search server will contain a series of indexes with the pattern _ghtracker-*_ that you can use in visualizations and dashboards.
