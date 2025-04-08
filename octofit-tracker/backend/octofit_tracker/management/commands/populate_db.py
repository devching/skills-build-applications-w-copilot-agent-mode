import logging
from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Command(BaseCommand):
    help = "Populate the database with test data"

    def handle(self, *args, **kwargs):
        try:
            # Create test users
            user1 = User.objects.create(email="user1@example.com", name="User One", password="password1")
            logger.info(f"Created user: {user1}")
            user2 = User.objects.create(email="user2@example.com", name="User Two", password="password2")
            logger.info(f"Created user: {user2}")

            # Create test teams
            team1 = Team.objects.create(name="Team Alpha", members=[user1.id, user2.id])
            logger.info(f"Created team: {team1}")
            team2 = Team.objects.create(name="Team Beta", members=[user2.id])
            logger.info(f"Created team: {team2}")

            # Create test activities
            activity1 = Activity.objects.create(activity_id="A1", user=user1, description="Running 5km")
            logger.info(f"Created activity: {activity1}")
            activity2 = Activity.objects.create(activity_id="A2", user=user2, description="Cycling 10km")
            logger.info(f"Created activity: {activity2}")

            # Create test leaderboard entries
            leaderboard1 = Leaderboard.objects.create(leaderboard_id="L1", team=team1, score=100)
            logger.info(f"Created leaderboard: {leaderboard1}")
            leaderboard2 = Leaderboard.objects.create(leaderboard_id="L2", team=team2, score=80)
            logger.info(f"Created leaderboard: {leaderboard2}")

            # Create test workouts
            workout1 = Workout.objects.create(workout_id="W1", name="Morning Yoga", duration=30)
            logger.info(f"Created workout: {workout1}")
            workout2 = Workout.objects.create(workout_id="W2", name="Evening Cardio", duration=45)
            logger.info(f"Created workout: {workout2}")

            self.stdout.write(self.style.SUCCESS("Database populated with test data."))
        except Exception as e:
            logger.error(f"Error populating database: {e}")
            raise