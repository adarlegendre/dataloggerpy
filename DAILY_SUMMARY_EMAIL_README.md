# Daily Summary Email System

This document explains the daily summary email system that sends aggregated radar detection data via email at scheduled times.

## Overview

The system automatically generates and sends a daily summary email containing:
- Total detections per radar
- ANPR (license plate) detection counts
- Breakdown by direction (e.g., "Towards Village" vs "Towards Town")
- Location coordinates (latitude/longitude)
- Date/time of detections

## Email Format

The email includes a JSON attachment with the following structure:

```json
[
  {
    "IMR_AD": "IMR_KD-BEKO",
    "name": "K Dubči",
    "route": "",
    "datetime": "2025-07-06T06:45:00.000Z",
    "lat": 50.063607443341105,
    "lon": 14.633117543618177,
    "detections": 50,
    "detections_ANPR": 48,
    "directions": [
      {
        "id": "IMR_KD-BE",
        "name": "K Běchovicům",
        "detections": 30,
        "detections_ANPR": 30
      },
      {
        "id": "IMR_KD-KO",
        "name": "Ke Kolodějskému zámku",
        "detections": 20,
        "detections_ANPR": 18
      }
    ]
  }
]
```

## Configuration

### 1. Database Migration

The new fields have been added to the `RadarConfig` model. Make sure migrations are applied:

```bash
python manage.py migrate
```

### 2. Radar Configuration

For each radar, you can now configure:
- **Route**: Route identifier (optional)
- **Latitude**: GPS latitude coordinate (optional)
- **Longitude**: GPS longitude coordinate (optional)

These can be configured in the Django admin interface or the configuration page.

### 3. Email Settings

Configure your email settings in the Notification Settings section:

1. Navigate to Configuration → Notification Settings
2. Fill in:
   - Primary email address
   - SMTP server details
   - SMTP credentials
   - Notification frequency (e.g., "daily")
3. Set notification times (e.g., "00:00" for midnight)
4. Enable notifications
5. Save settings

### 4. Cron Job Setup

The system uses cron jobs (Linux) or scheduled tasks (Windows) to check every minute whether it's time to send notifications.

#### Automatic Setup

When you save notification settings with notifications enabled, the system automatically:
- Creates/updates the cron job
- Schedules it to run every minute
- Checks if it's time to send based on your configured schedule

#### Manual Cron Job Setup (Linux)

```bash
python manage.py setup_cron_jobs
```

To remove cron jobs:

```bash
python manage.py setup_cron_jobs --remove
```

## Testing

### Test the Summary Email

Test the email generation and sending without waiting for the scheduled time:

```bash
# Test with yesterday's data (default)
python manage.py test_summary_email

# Test with a specific date
python manage.py test_summary_email --date 2025-01-15

# Preview the JSON without sending email
python manage.py test_summary_email --preview
```

### Test Email Connection

Test your SMTP settings:

```bash
python test_email.py
```

Or use the "Send Test Email" button in the Configuration page.

## Scheduling Options

### Daily at Midnight (00:00)

**Configuration:**
- Frequency: Daily
- Notification Times: `00:00`
- Days of the Week: (leave blank for all days)

### Multiple Times Per Day

**Configuration:**
- Frequency: Daily
- Notification Times: `00:00,12:00,18:00`
- Days of the Week: (leave blank for all days)

### Specific Days Only

**Configuration:**
- Frequency: Daily
- Notification Times: `00:00`
- Days of the Week: `Monday,Wednesday,Friday`

## How It Works

1. **Cron Job Runs**: Every minute, the cron job executes `check_notification_schedule` command
2. **Check Schedule**: The command checks if it's time to send based on:
   - Current time matches configured notification time
   - Current day matches configured days (if specified)
   - Sufficient time has passed since last notification (based on frequency)
3. **Generate Report**: If conditions are met, generates summary for the previous day
4. **Aggregate Data**: Collects all detections from active radars and groups by:
   - Radar
   - Direction
   - ANPR status
5. **Send Email**: Sends email with JSON attachment to configured recipients
6. **Track Status**: Records the notification in the database

## Data Aggregation Logic

The system:
- Only includes active radars
- Aggregates detections from the previous day (00:00 to 23:59:59)
- Counts total detections per radar
- Counts ANPR detections (where license plate was detected)
- Breaks down counts by direction (positive/negative)
- Uses the most recent detection time as the `datetime` field

## Troubleshooting

### Cron Job Not Running

Check cron status:
```bash
crontab -l | grep "Radar Notification"
```

Check logs:
```bash
tail -f logs/notification_service.log
```

### No Data in Email

Ensure:
- Radars are marked as active in configuration
- Detections exist in the database for the date range
- Run test command to verify: `python manage.py test_summary_email --preview`

### Email Not Sending

1. Test SMTP connection:
   ```bash
   python test_email.py
   ```

2. Check notification settings:
   - SMTP server and port are correct
   - Username and password are valid
   - TLS is enabled if required

3. Check logs:
   ```bash
   tail -f logs/notification_service.log
   ```

### Wrong Time Zone

The system uses Django's `TIME_ZONE` setting. Ensure it's configured correctly in `core/settings.py`:

```python
TIME_ZONE = 'UTC'  # or your local timezone
USE_TZ = True
```

## Manual Trigger

To manually trigger a notification check without waiting for the scheduled time:

```bash
python manage.py check_notification_schedule
```

This is useful for testing or troubleshooting.

## Database Models

### RadarConfig (Updated)

New fields:
- `route`: CharField (max 255, optional) - Route identifier
- `latitude`: FloatField (optional) - GPS latitude
- `longitude`: FloatField (optional) - GPS longitude

### EmailNotification

Tracks sent notifications:
- `notification_settings`: ForeignKey to NotificationSettings
- `start_date`: DateTime - Start of report period
- `end_date`: DateTime - End of report period
- `status`: Choice (pending/sent/failed)
- `sent_at`: DateTime - When email was sent

## API Functions

### `generate_daily_summary_report(start_date, end_date)`

Generates the summary data structure.

**Returns:** List of dictionaries with radar summaries

### `send_daily_summary_email(start_date, end_date, notification_settings=None)`

Sends the summary email.

**Returns:** Boolean (True if successful)

## Notes

- The system sends data for the **previous day** (yesterday)
- If you configure "00:00" as the notification time, it will send data from the day before yesterday
- Detections are counted based on their `start_time` field
- Only active radars are included in the summary
- If no detections exist for a day, no email is sent (or an empty summary is sent)

## Example Workflow

1. Configure radar with:
   - Name: "K Dubči"
   - IMR_AD: "IMR_KD-BEKO"
   - Route: "Route 123"
   - Latitude: 50.063607
   - Longitude: 14.633118
   - Direction Positive: "K Běchovicům" (ID: "IMR_KD-BE")
   - Direction Negative: "Ke Kolodějskému zámku" (ID: "IMR_KD-KO")

2. Configure notification settings:
   - Email: admin@example.com
   - Frequency: Daily
   - Time: 00:00
   - Enable notifications: ✓

3. Save settings (cron job is automatically created)

4. Every day at 00:00:
   - Cron job runs
   - System aggregates yesterday's detections
   - Email is sent with JSON attachment
   - Notification is logged in database

## Support

For issues or questions, check:
- Application logs: `logs/notification_service.log`
- Django logs
- Cron logs: Check the log file path shown in the Configuration page

