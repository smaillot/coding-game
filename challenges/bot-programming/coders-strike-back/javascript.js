function LimitPower(power)
{
    return Math.floor(Math.min(100,Math.max(0,power)));
}


function ComputePower2(Dcp,Acp)
{
    if (prevPow==-1)
    {
        return 'BOOST';
    }
    if (Acp<20)
    {
        return LimitPower(Dcp/10);
    }
    else
    {
        if (Dcp<5000)
        {
            return LimitPower(Dcp/200);
        }
        else
        {
            return LimitPower(100-100*Math.pow(Math.abs(Acp)/90,2));
        }
    }
}

function ComputePower(Dcp,angleSpeed,Acp)
{
    if(Dcp>5000 && Acp<5 && angleSpeed<10)
    {
        return "BOOST";
    }
    return LimitPower(100*Math.cos(Acp/180)*Math.min(1,Math.sqrt(Dcp*4)/100));
}

prevX=0;
prevY=0;

cpX=[];
cpY=[];
prevCpX=0;
prevCpY=0;

while (true) {
    var inputs = readline().split(' ');
    var x = parseInt(inputs[0]);
    var y = parseInt(inputs[1]);
    var nextCheckpointX = parseInt(inputs[2]); // x position of the next check point
    var nextCheckpointY = parseInt(inputs[3]); // y position of the next check point
    var nextCheckpointDist = parseInt(inputs[4]); // distance to the next checkpoint
    var nextCheckpointAngle = parseInt(inputs[5]); // angle between your pod orientation and the direction of the next checkpoint
    var inputs = readline().split(' ');
    var opponentX = parseInt(inputs[0]);
    var opponentY = parseInt(inputs[1]);

    Vx=x-prevX;
    Vy=x-prevY;
    var power=ComputePower(nextCheckpointDist,Math.acos((Vx*(nextCheckpointX-x)+Vy*(nextCheckpointY-y))/((Vx*Vx+Vy*Vy)*(Math.pow((nextCheckpointX-x),2)+Math.pow((nextCheckpointY-y),2)))),nextCheckpointAngle);
    prevX=x;
    prevY=y;

    print(nextCheckpointX + ' ' + nextCheckpointY + ' ' + power);
}
