sudo touch /tmp/.com.apple.dt.CommandLineTools.installondemand.in-progress
softwareupdate -l
# Update command line tools via software update.
sudo rm /tmp/.com.apple.dt.CommandLineTools.installondemand.in-progress