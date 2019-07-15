# Bill Split

CLI to split monthly bills.

## Usage

```bash
bill-split
```

## Configuration

The script expects a YAML file located at `$HOME/.bill-split.yml` that contains
a mapping of percentage splits expressed as whole numbers out of 100. For
example:

```yaml
---
splits:
  John: 25
  Anne: 25
  Mark: 50
```
