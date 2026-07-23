# ${{ values.name }}

## Overview

${{ values.description }}

## Ownership

- **Owner:** `${{ values.owner }}`
- **System:** `${{ values.system }}`
- **Lifecycle:** `${{ values.lifecycle }}`

## Architecture

```text
Client
  │
  ▼
${{ values.name }}
  │
  ▼
Downstream services and resources