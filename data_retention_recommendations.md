# 📊 Data Retention Recommendations

## Current Situation
- **Save Interval**: 5 minutes (configurable)
- **Retention**: Files saved permanently (no automatic cleanup)
- **Storage**: JSON files accumulate indefinitely

## Recommended Retention Policies

### Option 1: Automatic File Cleanup (Recommended)
Add to `app/services.py` or create a management command:

```python
def cleanup_old_files(days_to_keep=30):
    """Delete JSON files older than specified days"""
    from datetime import datetime, timedelta
    import os
    
    cutoff_date = datetime.now() - timedelta(days=days_to_keep)
    data_dir = 'data'
    
    deleted_count = 0
    for filename in os.listdir(data_dir):
        if filename.endswith('.json'):
            file_path = os.path.join(data_dir, filename)
            file_time = datetime.fromtimestamp(os.path.getmtime(file_path))
            
            if file_time < cutoff_date:
                os.remove(file_path)
                deleted_count += 1
                print(f"Deleted old file: {filename}")
    
    print(f"Cleaned up {deleted_count} old files")
```

### Option 2: Compress Old Files
```python
def compress_old_files(days_threshold=7):
    """Compress files older than threshold"""
    import gzip
    import shutil
    from datetime import datetime, timedelta
    
    cutoff_date = datetime.now() - timedelta(days=days_threshold)
    data_dir = 'data'
    
    for filename in os.listdir(data_dir):
        if filename.endswith('.json'):
            file_path = os.path.join(data_dir, filename)
            file_time = datetime.fromtimestamp(os.path.getmtime(file_path))
            
            if file_time < cutoff_date and not filename.endswith('.gz'):
                # Compress the file
                with open(file_path, 'rb') as f_in:
                    with gzip.open(f"{file_path}.gz", 'wb') as f_out:
                        shutil.copyfileobj(f_in, f_out)
                os.remove(file_path)
                print(f"Compressed: {filename}")
```

### Option 3: Database-Only Storage
```python
# Store only detections in database, skip JSON files
# Modify _save_data_to_file to only save to database
def _save_data_to_database_only(self, radar_id):
    """Save detections directly to database, skip JSON files"""
    # Process detections and save to RadarObjectDetection model
    # No JSON file creation
```

## Recommended Configuration

### For Production Use:
1. **Save Interval**: 5-10 minutes (good balance)
2. **Retention**: 30-90 days (depending on storage space)
3. **Cleanup**: Daily automated cleanup of old files
4. **Backup**: Weekly backup of recent files

### For Development:
1. **Save Interval**: 1-2 minutes (faster testing)
2. **Retention**: 7 days (shorter retention)
3. **Cleanup**: Manual cleanup as needed

## Implementation Steps

### 1. Create Management Command
```bash
python manage.py cleanup_old_files --days=30
```

### 2. Schedule with Cron
```bash
# Daily cleanup at 2 AM
0 2 * * * cd /path/to/project && python manage.py cleanup_old_files --days=30
```

### 3. Monitor Storage Usage
```bash
# Check data directory size
du -sh data/

# Count files
ls -1 data/*.json | wc -l
```

## Storage Estimates

### File Size Calculations:
- **Average file**: ~50KB (depends on traffic)
- **5-minute intervals**: 288 files/day
- **Daily storage**: ~14MB/day
- **Monthly storage**: ~420MB/month
- **Yearly storage**: ~5GB/year

### With 30-day retention:
- **Total files**: ~8,640 files
- **Total storage**: ~420MB

## Configuration Options

### In Django Admin:
1. Go to Radar Configuration
2. Set `file_save_interval` (1-60 minutes)
3. Consider reducing interval for less frequent saves

### In Settings:
```python
# Add to settings.py
DATA_RETENTION_DAYS = 30
AUTO_CLEANUP_ENABLED = True
COMPRESS_OLD_FILES = True
```

## Current Recommendations for Your System:

1. **Keep current 5-minute interval** (good balance)
2. **Implement 30-day retention** (reasonable storage usage)
3. **Add daily cleanup script** (automated management)
4. **Monitor disk usage** (prevent storage issues)

This will keep your system running smoothly while preserving recent data for analysis!
