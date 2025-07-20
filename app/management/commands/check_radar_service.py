from django.core.management.base import BaseCommand
from app.utils.startup_service import get_radar_service_status
from app.models import RadarConfig

class Command(BaseCommand):
    help = 'Check the status of the radar data collection service'

    def add_arguments(self, parser):
        parser.add_argument(
            '--start',
            action='store_true',
            help='Start the radar data collection service if not running',
        )
        parser.add_argument(
            '--restart',
            action='store_true',
            help='Restart the radar data collection service',
        )

    def handle(self, *args, **options):
        if options['restart']:
            self.stdout.write('Restarting radar data collection service...')
            try:
                from app.utils.startup_service import startup_service
                startup_service.stop_radar_data_collection()
                startup_service.start_radar_data_collection()
                self.stdout.write(
                    self.style.SUCCESS('Radar data collection service restarted successfully')
                )
            except Exception as e:
                self.stdout.write(
                    self.style.ERROR(f'Failed to restart radar data collection service: {str(e)}')
                )
            return

        if options['start']:
            self.stdout.write('Starting radar data collection service...')
            try:
                from app.utils.startup_service import initialize_radar_data_collection
                success = initialize_radar_data_collection()
                if success:
                    self.stdout.write(
                        self.style.SUCCESS('Radar data collection service started successfully')
                    )
                else:
                    self.stdout.write(
                        self.style.ERROR('Failed to start radar data collection service')
                    )
            except Exception as e:
                self.stdout.write(
                    self.style.ERROR(f'Failed to start radar data collection service: {str(e)}')
                )
            return

        # Get service status
        status = get_radar_service_status()
        
        self.stdout.write('Radar Data Collection Service Status')
        self.stdout.write('=' * 40)
        
        # Service status
        if status['started']:
            self.stdout.write(
                self.style.SUCCESS(f'Service Status: RUNNING')
            )
        else:
            self.stdout.write(
                self.style.ERROR(f'Service Status: STOPPED')
            )
        
        # Radar service status
        if status['radar_service']:
            self.stdout.write(f'Radar Service: {status["radar_service"].upper()}')
        else:
            self.stdout.write('Radar Service: INACTIVE')
        
        # Active radars
        self.stdout.write(f'Active Radars: {status["active_radars"]}')
        self.stdout.write(f'Active Threads: {status["active_threads"]}')
        self.stdout.write(f'Last Check: {status["last_check"]}')
        
        # Show configured radars
        self.stdout.write('\nConfigured Radars:')
        self.stdout.write('-' * 20)
        
        radars = RadarConfig.objects.all().order_by('id')
        if radars.exists():
            for radar in radars:
                status_icon = '🟢' if radar.is_active else '🔴'
                self.stdout.write(f'{status_icon} Radar {radar.id}: {radar.name}')
                self.stdout.write(f'    Port: {radar.port}')
                self.stdout.write(f'    Active: {radar.is_active}')
                self.stdout.write(f'    Update Interval: {radar.update_interval}ms')
                self.stdout.write(f'    File Save Interval: {radar.file_save_interval}min')
                self.stdout.write('')
        else:
            self.stdout.write('No radars configured')
        
        # Recommendations
        self.stdout.write('\nRecommendations:')
        self.stdout.write('-' * 15)
        
        if not status['started']:
            self.stdout.write(
                self.style.WARNING('• Service is not running. Use --start to start it.')
            )
        
        if status['active_radars'] == 0:
            self.stdout.write(
                self.style.WARNING('• No active radars found. Check radar configuration.')
            )
        
        if status['active_threads'] != status['active_radars']:
            self.stdout.write(
                self.style.WARNING('• Some radar threads may not be running properly.')
            )
        
        if status['started'] and status['active_radars'] > 0 and status['active_threads'] == status['active_radars']:
            self.stdout.write(
                self.style.SUCCESS('• All systems operational!')
            ) 