# @neo-flowoff/shared

Shared utilities for the NEO-FlowOFF ecosystem.

## Packages

### logger

Centralized logging utility with debug flag support.

**Usage:**

```typescript
import { logger } from "@neo-flowoff/shared/logger";

// Debug logs (only in development or when DEBUG=true)
logger.debug("TAG", "Debug message", { data: "value" });

// Info logs (always shown)
logger.info("TAG", "Info message");

// Warning logs (always shown)
logger.warn("TAG", "Warning message");

// Error logs (always shown)
logger.error("TAG", "Error message", error);
```

**Environment Variables:**

- `NODE_ENV=production` - Disables debug logs
- `DEBUG=true` - Enables debug logs even in production

## Installation

This package is part of the NEO-FlowOFF workspace. Install dependencies with:

```bash
pnpm install
```

## Development

```bash
# Run with debug logs
DEBUG=true pnpm dev

# Run in production mode
NODE_ENV=production pnpm start
```

