function threeplots()
    independent()
end

function independent()
    figure
    axis([-2 4 -2 4])
    hold on
    plot(xlim,[0 0],'k')
    plot([0 0],ylim,'k')
    plot([-2 4],[-2,4],'LineWidth',3)
    plot([-2 4],[4 -2],'b','LineWidth',3)
end


