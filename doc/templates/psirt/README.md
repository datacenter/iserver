# Cisco PSIRT

Uses [Cisco PSIRT openVuln API](https://developer.cisco.com/psirt/) calls to provide the security vulnerability information

## How to use

- Perform one-time API key/secret configuration
- Run 'iserver get psirt' without any parameters to get security vulnerabilities updated no longer than 1 year ago.
- Use --added and --updated flags to control max. age in days
- The output is limited to 25 entries by default. Use --limit option to change it. Use --limit 0 for unlimited output.
- Use filter options to select specific vulnerabilities. Multiple filtering options work with logical AND rule.
- Use view (-v) parameter to control what type of information you want to get onto the screen for the selected vulnerabilities.

## Filtering options

- [sev](PsirtFilterSev.md)
- [bug](PsirtFilterBug.md)
- [cve](PsirtFilterCve.md)
- [cwe](PsirtFilterCwe.md)
- [prod](PsirtFilterProd.md)
- [ver](PsirtFilterVer.md)
- [added](PsirtFilterAdded.md)
- [updated](PsirtFilterUpdated.md)

## View options
- [list](./PsirtViewList.md)
- [url](./PsirtViewUrl.md)
- [sum](./PsirtViewSum.md)
- [ver](./PsirtViewVer.md)
- [prod](./PsirtViewProd.md)
- [settings](./PsirtViewSettings.md)

## Output options
- [default](./PsirtOutputDefault.md)
- [json](./PsirtOutputJson.md)

## API authentication

iserver interacts with Cisco API console using REST API. Follow the [guide](https://developer.cisco.com/docs/psirt/#!authentication) in order to get key and secret .Values.day0.domain

Then perform one time configuration in iserver tool

```
$ iserver set psirt --key lalala --secret lalalala
Psirt api access configured

Psirt API settings
------------------
Enabled: True
Key: ***
Secret: ***
Cache: True
Directory: C:\Users\akaliwod\.itool\psirt-cache
TTL: 86400
```

## Cache

By default iserver caches locally all the security advisories received from Cisco API console with 1 day time-to-live.

Use 'iserver set --cache on|off' or 'iserver set --ttl <sec>' commands to control cache state and ttl.

## Command Options

```
DOC_TEMPLATE:get_psirt_filter.help:output
```

[[Back]](../../README.md)